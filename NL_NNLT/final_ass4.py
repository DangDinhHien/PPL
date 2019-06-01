    def visitFor_Final_exam(self,ast,o):

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        beginLabel = frame.getNewLabel()     

        frame.enterLoop()
        #initial value of variable(DO EXPR1)
        self.emit.printout(self.visit(ast.expr1,SubBody(frame, env)))
        #BEGIN FOR LOOP

        #BEGIN LABEL
        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        #check condition(DO EXPR2)
        self.emit.printout(self.visit(ast.expr2,SubBody(frame, env)))
        # if false break
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        list(map(lambda x:self.emit.printout(self.visit(x,SubBody(frame, env))) ,ast.loop)) 

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        #DO expr3
        self.emit.printout(self.visit(ast.expr3,SubBody(frame, env)))
        
        #GOTO BEGIN LABEL
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))

        #BREAK LABEL
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()

    def visitBinaryOp_Final_Exam(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym
        # Assum we have visit function for Exp(Ex: Id ,Inliteral etc... )
        str_left, type1 = self.visit(ast.left,Access(frame, nenv, False, False))  
        str_right, type2 = self.visit(ast.right,Access(frame, nenv, False, False))
        ###################
        result = []
        label_exit_compare = frame.getNewLabel()
        label_go_on = frame.getNewLabel()
        

        result.append(str_left)
        result.append(self.emit.emitIFFALSE(label_exit_compare, frame))
        result.append(str_right)
        result.append(self.emit.emitIFFALSE(label_exit_compare, frame))

        # if both of them is True -> return True
        result.append(self.emitPUSHCONST(1, IntType(), frame))
        result.append(self.emitGOTO(label_go_on,frame))

        # if either of them is False -> return False
        #LABEL EXIT
        result.append(self.emitLABEL(label_exit_compare,frame))
        result.append(self.emitPUSHCONST(0, IntType(), frame))
        #LABEL GO ON
        result.append(self.emitLABEL(label_go_on,frame))  

        return ''.join(result),BoolType()


    def visitFor_ASS4_MP(self,ast,o):
        # o is SubBody
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        forLabel = frame.getNewLabel()
        frame.enterLoop()

        lst = list()
        if str(ast.up) == "True":
            lst = ["<=","+"]
        else:
            lst = [">=","-"]

        indx = frame.getNewIndex()

        self.emit.printout(self.emit.emitPUSHICONST(ast.expr1.value,frame))#ipush_1
        self.emit.printout(self.emit.emitWRITEVAR("temp",IntType(),indx,frame))# istore_indx

        self.emit.printout(self.emit.emitLABEL(forLabel,frame))

        #find value of id 
        id_ = self.lookup(ast.id.name,o.sym,lambda x:x.name) #symbol
        indx_id = id_.value.value

        #Reassign value for i 
        self.emit.printout(self.emit.emitREADVAR("temp",IntType(),indx,frame)) 
        self.emit.printout(self.emit.emitWRITEVAR(ast.id,IntType(),indx_id,frame))
        #check condition
        self.emit.printout(self.emit.emitREADVAR(ast.id,IntType(),indx,frame)) 
        self.emit.printout(self.emit.emitPUSHICONST(ast.expr2.value,frame))
        self.emit.printout(self.emit.emitREOP("<=", IntType(), frame))
        #if False -> break
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        list(map(lambda x: self.visit(x,o),ast.loop))
        # CONTINUE LABEL
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(),frame))
        # INCREMENT temp variable
        self.emit.printout(self.emit.emitREADVAR("temp",IntType(),indx,frame)) 
        self.emit.printout(self.emit.emitPUSHICONST(1,frame))
        self.emit.printout(self.emit.emitADDOP("+",IntType(),frame))
        self.emit.printout(self.emit.emitWRITEVAR("temp",IntType(),indx,frame))
        # GOTO FOR LABEL
        self.emit.printout(self.emit.emitGOTO(forLabel,frame))
        # BREAK LABEL
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop() 